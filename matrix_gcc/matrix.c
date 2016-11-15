int main(){
	//matrix
	int N = 10;
	int M = 10;
	
	//vector
	int c_i;

	for (int i=0; i < N-1; i=i+1){
		c_i = 0;
		for (int j=0; i < M-1; j=j+1){
			c_i += accessMatrixA(i,j)*accessArrayB(j);
		}
	}
}
int accessMatrixA(int i, int j){
	int a_i_j;
	// Matrix code
	return a_i_j;
}
int accessArrayB(int i){
	int b_i;
	// Array code
	return b_i;
}
int accessArrayC(int i){
	int c_i;
	// Array code
	return c_i;
}