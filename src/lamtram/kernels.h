#include <thrust/sort.h>
#include <thrust/execution_policy.h>

void set_softmax(float* softmax, float value);

void sort_list(float* softmax, int len);
