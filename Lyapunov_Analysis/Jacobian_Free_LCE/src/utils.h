// Enda Carroll
// May 2020
// Header file for utility functions in utils.c

// ---------------------------------------------------------------------
//  Standard Libraries and Headers
// ---------------------------------------------------------------------


// ---------------------------------------------------------------------
//  User Libraries and Headers
// ---------------------------------------------------------------------


// ---------------------------------------------------------------------
//  Function Prototypes
// ---------------------------------------------------------------------

int max_indx_d(double* array, int n);

void write_array(double *A, int n, char *filename);
void write_array_fftwreal(fftw_complex *A, int n, char *filename);
void write_array_fftwimag(fftw_complex *A, int n, char *filename);


void print_array_1d_d(double* arr, char* arr_name, int n);
void print_array_2d_d(double* arr, char* arr_name, int r, int c);

void print_array_1d_z(fftw_complex* arr, char* arr_name, int n);
void print_array_2d_z(fftw_complex* arr, char* arr_name, int r, int c);




