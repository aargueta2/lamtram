#include "kernels.h"

__global__ void hello(float *softmax)
{
  softmax[threadIdx.x] = 1.0;

}


void set_softmax(float* softmax, float value)
{

}

void sort_list(float* softmax, int len){
  //thrust::device_ptr<int> thrust_softmax = thrust::device_pointer_cast(softmax);
  //thrust::sort(softmax, softmax + len);
}
