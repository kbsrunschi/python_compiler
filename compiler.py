#!/usr/bin/python
     
'''
Kathryn Smith & Logan Young
Programming Assignment 4
  
'''
     
import ply.lex as lex
import ply.yacc as yacc
import sys
import LinkedList as ll
import ply.cpp
import time
     
#Pre-Processor
fileinpath = sys.argv[1]
fileoutpath = "%s.s"%fileinpath[:-6]
     
filein = open(fileinpath, 'r')
macroMap = {}
includeMap = {}
filetext = ""
for line in filein:
    if line.startswith("#define"):
        splitline = line.split(" ")
        macroMap[splitline[1]] = splitline[2][:-2]
    elif line.startswith("# "):
        pass
    #filetext += line
    elif line.startswith("#include"):
        splitline = line.split(" ")
        includeMap[0] = splitline[1][1:-2]
        #filetext += line
        print "We are including these file(s): ", includeMap
    else:
        filetext += line
filein.close()
for key in macroMap.keys():
    filetext = filetext.replace(key, macroMap[key])
     
errorList = []
     
#print macroMap
     
#Tokenizer
tokens= (
    'COMMENT',
    'INTEGER_DECLARATION',
    'STRING_DECLARATION',
    'EXTERN_DECLARATION',
    'CONST_INT',
    'IF',
    'ELSE',
    'DO',
    'WHILE',
    'FOR',
    'RETURN',
    'CONST_STRING',
    'PLUS',
    'MINUS',
    'MULTI',
    'DIV',
    'MODULO',
    'SHIFTLEFT',
    'SHIFTRIGHT',
    'EGAL',
    'DIFF',
    'INF',
    'SUP',
    'INFEQUAL',
    'SUPEQUAL',
    'RIGHT_BRACKET',
    'LEFT_BRACKET',
    'RIGHT_PARENTHESIS',
    'LEFT_PARENTHESIS',
    'COMMA',
    'SEMICOLON',
    'IDENT',
    'ASSIGNMENT'
)
     
def t_ignore_COMMENT(t):
    r'//.*\n|/\*.*\*/'
    pass
     
def t_INTEGER_DECLARATION(t):
    r'int'
    return t
     
def t_STRING_DECLARATION(t):
    r'string'
    return t
     
def t_EXTERN_DECLARATION(t):
    r'extern'
    return t
     
def t_IF(t):
    r'if'
    return t
     
def t_ELSE(t):
    r'else'
    return t
     
def t_WHILE(t):
    r'while'
    return t
     
def t_DO(t):
    r'do'
    return t
     
def t_FOR(t):
    r'for'
    return t
     
def t_RETURN(t):
    r'return'
    return t
     
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTI = r'\*'
t_DIV = r'/'
t_MODULO = r'%'
t_SHIFTLEFT = r'\<\<'
t_SHIFTRIGHT = r'\>\>'
     
t_COMMA = r','
     
def t_EGAL(t):
    r'=='
    return t
     
t_DIFF = r'!='
t_INF = r'\<'
t_SUP = r'\>'
t_INFEQUAL = r'\<='
t_SUPEQUAL = r'\>='
     
def t_ASSIGNMENT(t):
    r'='
    return t
     
def t_LEFT_PARENTHESIS(t):
    r'\('
    return t
     
def t_RIGHT_PARENTHESIS(t):
    r'\)'
    return t
     
def t_LEFT_BRACKET(t):
    r'\{'
    return t
     
def t_RIGHT_BRACKET(t):
    r'\}'
    return t
     
def t_SEMICOLON(t):
    r';'
    return t
     
def t_CONST_INT(t):
    r'\d+(\.\d+)?'
    return t
     
def t_IDENT(t):
    r'[a-zA-Z_][\d_a-zA-Z]*'
    return t
     
t_CONST_STRING = r'\"[^\"]*\"|\'[^\']*\''
     
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass
     
def t_ignore_SPACE(t):
    r'\s'
    pass
     
def t_error(t):
    print "Illegal expression %s at line %d" %(t.value[0], t.lexer.lineno)
    t.lexer.skip(1)
     

#for token in lexer:
#   print token
     
#Parser
stList = ll.LinkedList()
#External symbol table
stList.insert({})
#Global symbol table
stList.insert({})
     
global paramList
paramList = []
global curType
curType = 'nd'
global curFuncDecl
curFuncDecl = ()
global curLabel
curLabel = 0
global curIfLabel
curIfLabel = 0
global stringList
stringList = []
global curString
curString = 0
   
registerDict = {}
global  compilerPass
compilerPass = 0
     
precedence = (
    ('left', 'LEFT_PARENTHESIS'),
    ('right', 'RIGHT_PARENTHESIS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTI', 'DIV')
)
     
def p_program(p):
    '''program : external_declaration
    | program external_declaration'''
    #print 'Program grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = p[1] + p[2]
     
def p_external_declaration(p):
    '''external_declaration : declaration
    | EXTERN_DECLARATION declaration
    | function_definition'''
    #print 'external declaration grammar!'
    global paramList, compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p[1]) <= 6:
            paramList = []
            decln = "NULL"
            curTable = "NULL"
            if len(p) == 2:
                decln = p[1]
                curTable = stList.tail
            elif len(p) == 3:
                decln = p[2]
                curTable = stList.head
            for declr in decln[1]:
                if declr[0] == 'var_decl':
                    if declr[1] in curTable.data.keys():
                        print 'UNIQUENESS ERROR: external variable ' + declr[1] + " is already defined."
                        errorList.append('UNIQUENESS ERROR: external variable ' + declr[1] + " is already defined.")
                    else:
                        curTable.data[declr[1]] = (decln[0],'', curTable.offSet)
                        curTable.offSet -= 4
                elif declr[0] == 'func_decl':
                    if declr[1] in curTable.data.keys():
                        print 'UNIQUENESS ERROR: external function ' + declr[1] + " is already defined."
                        errorList.append('UNIQUENESS ERROR: external function ' + declr[1] + " is already defined.")
                    else:
                        curTable.data[declr[1][0]] = (decln[0],declr[1][1], '')
            p[0] = ''
        else:
            p[0] = p[1]
     
def p_function_definiton(p):
    '''function_definition : type function_declarator decl_glb_fct compound_instruction'''
    #print 'function definition grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        p[0] = '\n' + p[2][1][0] + ':\n\tpush %ebp\n\tmovl %esp, %ebp\n\tsubl $' + str(p[4][1] * -1) + ', %esp'
        p[0] += p[4][0]
     
def p_decl_glb_fct(p):
    '''decl_glb_fct : '''
    global curFuncDecl, curType, compilerPass
    #print "declare global function grammar!"
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if curFuncDecl[1] in stList.tail.data.keys():
            print 'UNIQUENESS ERROR: external function ' + curFuncDecl[1] + " is already defined."
            errorList.append('UNIQUENESS ERROR: external function ' + curFuncDecl[1] + " is already defined.")
        else:
            stList.tail.data[curFuncDecl[1][0]] = (curType,curFuncDecl[1][1])
        p[0] = ''
     
def p_declaration(p):
    '''declaration : type declarator_list SEMICOLON'''
    #print 'declaration grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        p[0] = (p[1], p[2])
     
def p_type(p):
    '''type : INTEGER_DECLARATION
    | STRING_DECLARATION'''
    #print 'type grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        p[0] = p[1]
        global curType
        curType = p[0]
     
def p_declarator_list(p):
    '''declarator_list : declarator
    | declarator_list COMMA declarator'''
    #print 'declarator list grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = (p[1],)
        elif len(p) == 4:
            p[0] = p[1] + (p[3],)
     
def p_declaration_list(p):
    '''declaration_list : declaration
    | declaration_list declaration'''
    #print 'declaration list grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        stList.tail.offSet = -4
        if len(p) == 2:
            for declr in p[1][1]:
                if declr[0] == 'var_decl':
                    if declr[1] in stList.tail.data.keys():
                        print 'UNIQUENESS ERROR: variable ' + declr[1] + " is already defined."
                        errorList.append('UNIQUENESS ERROR: variable ' + declr[1] + " is already defined.")
                    else:
                        stList.tail.data[declr[1]] = (p[1][0],'',stList.tail.offSet)
                        stList.tail.offSet -= 4
                elif declr[0] == 'func_decl':
                    if declr[1] in stList.tail.data.keys():
                        print 'UNIQUENESS ERROR: function ' + declr[1] + " is already defined."
                        errorList.append('UNIQUENESS ERROR: function ' + declr[1] + " is already defined.")
                    else:
                        stList.tail.data[declr[1][0]] = (p[1][0],declr[1][1],'')
            p[0] = ('decln_list', (p[1],))
        elif len(p) == 3:
            for declr in p[2][1]:
                if declr[0] == 'var_decl':
                    if declr[1] in stList.tail.data.keys():
                        print 'UNIQUENESS ERROR: variable ' + declr[1] + " is already defined."
                        errorList.append('UNIQUENESS ERROR: variable ' + declr[1] + " is already defined.")
                    else:
                        stList.tail.data[declr[1]] = (p[2][0],'', stList.tail.offSet)
                        stList.tail.offSet -= 4
                elif declr[0] == 'func_decl':
                    if declr[1] in stList.tail.data.keys():
                        print 'UNIQUENESS ERROR: function ' + declr[1] + " is already defined."
                        errorList.append('UNIQUENESS ERROR: function ' + declr[1] + " is already defined.")
                    else:
                        stList.tail.data[declr[1][0]] = (p[2][0],declr[1][1], '')
            p[0] = ('decln_list', p[1][1] + (p[2],))
     
def p_declarator(p):
    '''declarator : IDENT
    | function_declarator'''
    #print 'declarator grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if isinstance(p[1], basestring):
            p[0] = ('var_decl', p[1])
        else:
            p[0] = p[1]
     
def p_function_declarator(p):
    '''function_declarator : IDENT LEFT_PARENTHESIS RIGHT_PARENTHESIS
    | IDENT LEFT_PARENTHESIS parameter_list RIGHT_PARENTHESIS'''
    #print 'function declarator grammar!'
    global paramList, compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 4:
            p[0] = ('func_decl', (p[1], ('param_list', ())))
        elif len(p) == 5:
            for num in range(0,len(p[3][1])):
                paramList.append(p[3][1][len(p[3][1]) - 1 - num])
            p[0] = ('func_decl', (p[1], p[3]))
        global curFuncDecl
        curFuncDecl = p[0]
     
def p_parameter_list(p):
    '''parameter_list : parameter_declaration
    | parameter_list COMMA parameter_declaration'''
    #print 'parameter list grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = ('param_list', (p[1],))
        elif len(p) == 4:
            p[0] = ('param_list', p[1][1] + (p[3],))
     
def p_instruction(p):
    '''instruction : SEMICOLON
    | compound_instruction
    | expression_instruction
    | iteration_instruction
    | select_instruction
    | jump_instruction'''
    #print 'instruction grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if p[1] != ';':
            if type(p[1]) is str:
                p[0] = p[1]
            elif type(p[1]) is tuple:
                p[0] = p[1][0]
        else:
            p[0] = ''
     
def p_expression_instruction(p):
    '''expression_instruction : expression SEMICOLON
    | assignment SEMICOLON'''
    #print 'expression instruction grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if p[1][0] == 'assign':
            p[0] = p[1]
        else:
            p[0] = p[1]
     
def p_parameter_declaration(p):
    '''parameter_declaration : type IDENT'''
    #print 'parameter declaration grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        p[0] = (p[1], p[2])
     
def p_assignment(p):
    '''assignment : IDENT ASSIGNMENT expression'''
    #print 'assignment grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        arg1Type = declaredAs(p[1])
        arg2Type = p[3][1]
        if arg1Type == 'nd':
            print 'NAME ERROR: ' + p[1] + ' has not been declared.'
            errorList.append('NAME ERROR: ' + p[1] + ' has not been declared.')
        elif arg1Type != arg2Type:
            print 'TYPE ERROR: Argument 1 has type ' + arg1Type + ', argument 2 has type ' + arg2Type + '.'
            errorList.append('TYPE ERROR: Argument 1 has type ' + arg1Type + ', argument 2 has type ' + arg2Type + '.')
        p[0] = p[3][0] + '\n\tpop ' + str(getOffset(p[1])) + '(%ebp)'
     
def p_compound_instruction(p):
    '''compound_instruction : block_start declaration_list instruction_list block_end
    | block_start declaration_list block_end
    | block_start instruction_list block_end
    | block_start block_end'''
    #print 'compound instruction grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 3:
            p[0] = ('',p[2])
        elif len(p) == 4:
            if p[2] == 'decln_list':
                p[0] = ('', p[3])
            else:
                p[0] = (p[2], p[3])
        elif len(p) == 5:
            p[0] = (p[3], p[4])
     
def p_block_start(p):
    '''block_start : LEFT_BRACKET'''
    #print 'block start grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
    #Create a new symbol table
        global paramList
        stList.insert({})
        argOffset = 4
        for param in paramList:
            stList.tail.data[param[1]] = (param[0],'', argOffset)
            stList.tail.offSet += 4
        paramList = [] 
        p[0] = p[1]
     
def p_block_end(p):
    '''block_end : RIGHT_BRACKET'''
    #print 'block end grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        #Remove this scope's symbol table
        offSet = stList.tail.offSet
        del stList.tail.data
        stList.delete()
        p[0] = offSet
     
def p_instruction_list(p):
    '''instruction_list : instruction
    | instruction_list instruction'''
    #print 'instruction list grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = p[1] + p[2]
     
def p_select_instruction(p):
    '''select_instruction : cond_instruction instruction
    | cond_instruction instruction ELSE instruction'''
    #print 'select instruction grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        global curIfLabel
        inverse = 'NULL'
        if 'jne' in p[1]:
            inverse = p[1].replace('jne', 'je')
        elif 'je' in p[1]:
            inverse = p[1].replace('je', 'jne')
        elif 'jge' in p[1]:
            inverse = p[1].replace('jge', 'jl')
        elif 'jle' in p[1]:
            inverse = p[1].replace('jle', 'jg')
        elif 'jl' in p[1]:
            inverse = p[1].replace('jl', 'jge')
        elif 'jg' in p[1]:
            inverse = p[1].replace('jg', 'jle')
        if len(p) == 3:
            p[0] = inverse + '.END' + str(curIfLabel) + p[2] + '\n.END' + str(curIfLabel) + ':'
            curIfLabel += 1
        if len(p) == 5:
            p[0] = inverse + '.ELSE' + str(curIfLabel) + p[2] + '\n\tjmp .END' + str(curIfLabel)
            p[0] += '\n.ELSE' + str(curIfLabel) + ':' + p[4] + '\n.END' + str(curIfLabel) + ':'
            curIfLabel += 1
     
def p_cond_instruction(p):
    '''cond_instruction : IF LEFT_PARENTHESIS condition RIGHT_PARENTHESIS'''
    #print 'cond instruction grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        p[0] = p[3]
     
def p_iteration_instruction(p):
    '''iteration_instruction : WHILE LEFT_PARENTHESIS condition RIGHT_PARENTHESIS instruction
    | DO instruction WHILE LEFT_PARENTHESIS condition RIGHT_PARENTHESIS
    | FOR LEFT_PARENTHESIS assignment SEMICOLON condition SEMICOLON assignment RIGHT_PARENTHESIS instruction'''
    #print 'iteration instruction grammar!'
    global compilerPass, curLabel
    if compilerPass == 0:
        if len(p) == 10:
            splitCond = p[5].split(' ')
            identifier = splitCond[0]
            comparand = splitCond[2]
            splitAssignment = p[7].split('=')
            expression = splitAssignment[1]
            if 'for' not in p[9] and comparand.isdigit() and expression[-1:]=='1':
                comparandVal = int(comparand)
                newInstruction = p[9][1:-1]
                newInstruction += p[9].replace(identifier + ' ', identifier + ' + 1 ')[1:-1]
                newInstruction += p[9].replace(identifier + ' ', identifier + ' + 2 ')[1:-1]
                newInstruction += p[9].replace(identifier + ' ', identifier + ' + 3 ')[1:-1]
                newInstruction += p[9].replace(identifier + ' ', identifier + ' + 4 ')[1:-1]
                p[9] = '{' + newInstruction + '}'
                p[7] = p[7][:-1] + '5'
        p[0] = ''
        for num in range(1, len(p)): 
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 6:
            p[0] = '\n.LOOP' + str(curLabel) + ':' + p[3]
            p[0] += '.BODY' + str(curLabel) + '\n\tjmp .LOOPEND' + str(curLabel) + '\n.BODY' + str(curLabel) + ':'
            p[0] += p[5] + '\n\tjmp .LOOP' + str(curLabel) + '\n.LOOPEND' + str(curLabel) + ':'
            curLabel += 1
        if len(p) == 7:
            p[0] = '\n.BODY' + str(curLabel) + ':' + p[2]
            p[0] += '\n.LOOP' + str(curLabel) + ':' + p[5]
            p[0] += '.BODY' + str(curLabel)
            curLabel += 1
        if len(p) == 10:
            p[0] = p[3]
            p[0] += '\n.LOOP' + str(curLabel) + ':' + p[5]
            p[0] += '.BODY' + str(curLabel) + '\n\tjmp .LOOPEND' + str(curLabel) + '\n.BODY' + str(curLabel) + ':'
            p[0] += p[9] + p[7] + '\n\tjmp .LOOP' + str(curLabel) + '\n.LOOPEND' + str(curLabel) + ':'
            curLabel += 1
     
def p_jump_instruction(p):
    '''jump_instruction : RETURN expression SEMICOLON '''
    #print 'jump instruction grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        argType = p[2][1]
        if argType != 'int' and argType != 'string':
            print 'TYPE ERROR: Cannot jump to ' + argType + '.'
            errorList.append('TYPE ERROR: Cannot jump to ' + argType + '.')
        p[0] = p[2][0] + '\n\tmovl %ebp, %esp\n\tpop %ebp\n\tret'
     
def p_condition(p):
    '''condition : expression comparison_operator expression'''
    #print 'condition grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        arg1Type = p[1][1]
        arg2Type = p[3][1]
        if arg1Type != arg2Type:
            print 'TYPE ERROR: No comparitive operation known for ' + arg1Type + ' and ' + arg2Type +'.'
            errorList.append('TYPE ERROR: No comparitive operation known for ' + arg1Type + ' and ' + arg2Type +'.')
        compCode = '\n\taddl $4, %esp\n\tcmpl %esp, 4(%esp)\n\taddl $4, %esp\n\t'
        if p[2] == '==':
            compCode += 'je'
        elif p[2] == '!=':
            compCode += 'jne'
        elif p[2] == '<':
            compCode += 'jl'
        elif p[2] == '>':
            compCode += 'jg'
        elif p[2] == '<=':
            compCode += 'jle'
        elif p[2] == '>=':
            compCode += 'jge'
        compCode += ' '
        p[0] = p[1][0] + p[3][0] + compCode
     
def p_comparison_operator(p):
    '''comparison_operator : EGAL
    | DIFF
    | INF
    | SUP
    | INFEQUAL
    | SUPEQUAL'''
    #print 'comparison operator grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        p[0] = p[1]
     
def p_expression(p):
    '''expression : expression_additive
    | expression SHIFTLEFT expression_additive
    | expression SHIFTRIGHT expression_additive'''
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    #print 'expression grammar!'
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            arg1Type = p[1][1]
            arg2Type = p[3][1]
            if arg1Type != 'int' or arg2Type != 'int':
                print 'TYPE ERROR: No shift operation known for ' + arg1Type + ' and ' + arg2Type +'.'
                errorList.append('TYPE ERROR: No shift operation known for ' + arg1Type + ' and ' + arg2Type +'.')
            if p[2] == '<<':
                p[0] = (p[1][0] + p[3][0] + '\n\taddl $4, %esp\n\tshl %esp, $4(%esp)', 'int')
            elif p[2] == '>>':
                p[0] = (p[1][0] + p[3][0] + '\n\taddl $4, %esp\n\tshr %esp, $4(%esp)', 'int')
     
def p_expression_additive(p):
    '''expression_additive : expression_multiplicative
    | expression_additive PLUS expression_multiplicative
    | expression_additive MINUS expression_multiplicative'''
    #print 'expression additive grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            arg1Type = p[1][1]
            arg2Type = p[3][1]
            if p[2] == '+':
                if arg1Type == 'int' and arg2Type == 'int':
                    p[0] = (p[1][0] + p[3][0] + '\n\taddl $4, %esp\n\taddl %esp, 4(%esp)', 'int')
                else:
                    if (arg1Type == 'int' and arg2Type == 'string') or (arg2Type == 'int' and arg1Type == 'string') or (arg1Type == 'string' and arg2Type == 'string'):
                        p[0] = (p[1][0] + p[3][0] + '\n\tcall strcat', 'string')
                    else:
                        print 'TYPE ERROR: No addition operation known for ' + arg1Type + ' and ' + arg2Type +'.'
                        errorList.append('TYPE ERROR: No addition operation known for ' + arg1Type + ' and ' + arg2Type +'.')
            elif p[2] == '-':
                if arg1Type != 'int' or arg2Type != 'int':
                    print 'TYPE ERROR: No subtraction operation known for ' + arg1Type + ' and ' + arg2Type +'.'
                    errorList.append('TYPE ERROR: No subtraction operation known for ' + arg1Type + ' and ' + arg2Type +'.')
                p[0] = (p[1][0] + p[3][0] + '\n\taddl $4, %esp\n\tsubl %esp, 4(%esp)', 'int')
     
def p_expression_multiplicative(p):
    '''expression_multiplicative : unary_expression
    | expression_multiplicative MULTI unary_expression
    | expression_multiplicative DIV unary_expression
    | expression_multiplicative MODULO unary_expression'''
    #print 'expression multiplicative grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            arg1Type = p[1][1]
            arg2Type = p[3][1]
            if p[2] == '*':
                if arg1Type != 'int' or arg2Type != 'int':
                    print 'TYPE ERROR: No multiplication operation known for ' + arg1Type + ' and ' + arg2Type +'.'
                    errorList.append('TYPE ERROR: No multiplication operation known for ' + arg1Type + ' and ' + arg2Type +'.')
                p[0] = (p[1][0] + p[3][0] + '\n\taddl $4, %esp\n\timull %esp, 4(%esp)', 'int') 
            elif p[2] == '/':
                if arg1Type != 'int' or arg2Type != 'int':
                    print 'TYPE ERROR: No division operation known for ' + arg1Type + ' and ' + arg2Type +'.'
                    errorList.append('TYPE ERROR: No division operation known for ' + arg1Type + ' and ' + arg2Type +'.')
                p[0] = (p[1][0] + p[3][0] + '\n\taddl $4, %esp\n\tmovl $0, %eax\n\tmovl 4(%esp), %eax\n\tdivl %esp\n\tmovl %eax, 4(%esp)', 'int')
            elif p[2] == '%':
                if arg1Type != 'int' or arg2Type != 'int':
                    print 'TYPE ERROR: No modulo operation known for ' + arg1Type + ' and ' + arg2Type +'.'
                    errorList.append('TYPE ERROR: No modulo operation known for ' + arg1Type + ' and ' + arg2Type +'.')
                p[0] = (p[1][0] + p[3][0] + '\n\taddl $4, %esp\n\tmovl $0, %edx\n\tmovl 4(%esp), %eax\n\tdivl %esp\n\tmovl %edx, 4(%esp)', 'int')
     
def p_unary_expression(p):
    '''unary_expression : expression_postfixee
    | MINUS unary_expression'''
    #print 'unary expression grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            argType = p[2][1]
            if argType != 'int':
                print 'TYPE ERROR: No negative operation known for ' + argType + '.'
                errorList.append('TYPE ERROR: No negative operation known for ' + argType + '.')
            p[0] = (p[2][0] + '\n\tnegl 4(%esp)', 'int')
     
def p_argument_expression_list(p):
    '''argument_expression_list : expression
    | argument_expression_list COMMA expression'''
    #print 'argument expression list grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = p[1] + p[3]
     
def p_expression_postfixee(p):
    '''expression_postfixee : primary_expression
    | IDENT LEFT_PARENTHESIS argument_expression_list RIGHT_PARENTHESIS
    | IDENT LEFT_PARENTHESIS RIGHT_PARENTHESIS '''
    #print 'expression postfixee grammar!'
    global compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            '''if p[1][0].isdigit():
                p[0] = ('\n\tpush $' + str(p[1][0]), p[1][1])
            elif p[1][0][0] == '\"' or p[1][0][0] == '\'':
                print stringList, p[1]
                p[0] = ('\n\tpush $.s' + str(stringList.index(p[1][0])), p[1][1])
            else:
                if p[1][1] == 'int':
                    p[0] = ('\n\tpush ' + str(getOffset(p[1][0])) + '(%ebp)', p[1][1])
                elif p[1][1] == 'string':
                    p[0] = ('\n\tpush $.s' + str(getOffset(p[1][0])), p[1][1])'''
            p[0] = p[1]
        elif len(p) == 4:
            argType = declaredAs(p[1])
            p[0] = ('\n\tcall ' + p[1], argType)
        elif len(p) == 5:
            argType = declaredAs(p[1])
            p[0] = (p[3][0] + '\n\tcall ' + p[1], argType)
     
def p_primary_expression(p):
    '''primary_expression : IDENT
    | CONST_INT
    | CONST_STRING
    | LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
    '''
    #print 'primary expression grammar!'
    global stringList, compilerPass
    if compilerPass == 0:
        p[0] = ''
        for num in range(1, len(p)):
            p[0] += p[num] + ' '
        p[0] = p[0][:-1]
    if compilerPass == 1:
        if len(p) == 2:
            if p[1].isdigit():
                p[0] = ('\n\tpush $' + p[1], 'int')
            elif p[1][0] == '\"' or p[1][0] == '\'':
                stringList.append(p[1])
                p[0] = ('\n\tpush $.s' + str(stringList.index(p[1])), 'string')
            else:
                argType = declaredAs(p[1])
                if argType == 'nd':
                    print 'NAME ERROR: ' + p[1] + ' is not declared.'
                    errorList.append('NAME ERROR: ' + p[1] + ' is not declared.')
                p[0] = ('\n\tpush ' + str(getOffset(p[1])) + '(%ebp)', argType)
        elif len(p) == 4:
            p[0] = p[2]
     
def p_error(p):
    print "Syntax error with " + str(p) + "."
     
def declaredAs(ident):
    for st in stList:
        if ident in st.keys():
            return st[ident][0]
    return 'nd' #not declared
     
def getOffset(ident):
    for st in stList:
        if ident in st.keys():
            return st[ident][2]
    errorList.append(ident)
    return -1

#for token in lexer:
#    print token.value + ' : ' + token.type + ' : ' + str(token.lexpos)


begin = time.clock()
lexer = lex.lex()
lexer.input(filetext)
parser = yacc.yacc()
outputFirstPass = parser.parse()


lexer = lex.lex()
lexer.input(outputFirstPass)

compilerPass = 1
output =  parser.parse()

end = time.clock()
elapsed = end - begin
print "Total Optimized Time: " + str(elapsed)

if len(stringList) != 0:
    output += '\n.section\t\t.rodata\n\t'
for num in range(0,len(stringList)):
    output += '.s' + str(num) + '\t.string ' + stringList[num] + '\n\t'
  
  
if len(errorList)==0:
    fileout = open(fileoutpath, 'w')
    fileout.write('\t.section    __TEXT,__text,regular,pure_instructions\n\t.macosx_version_min 10, 11\n\t.globl  _main\n\t.align  4, 0x90')
    fileout.write(output)
    fileout.close()
else:
    for error in errorList:
        print error