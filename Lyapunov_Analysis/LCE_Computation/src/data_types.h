// Enda Carroll
// May 2020
// Header file for global definitions, global parameters etc




// ---------------------------------------------------------------------
//  Output Datasets
// ---------------------------------------------------------------------
// #define __TRIADS
// #define __MODES
// #define __REALSPACE
// #define __LCE_ERROR
// #define TRANSIENT			// Turn on transient iterations - these iterations are ignored in the calculation



// ---------------------------------------------------------------------
//  Parameters
// ---------------------------------------------------------------------
#define SAVE_DATA_STEP 100	// Parameter to determine after how many integrations steps data should be saved to output
#define SAVE_LCE_STEP  10   // Parameter to determine how often to save LCE data
// #ifdef __TRANSIENT
// #define TRANS_STEPS 1000    // Set the transient iterations to perform
// #endif