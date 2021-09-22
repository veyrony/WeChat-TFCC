#include <iostream>

#define TFCC_WITH_MKL 1
#include "tfcc.h"
#ifdef TFCC_WITH_MKL
#include "utils/tfcc_mklutils.h"
#else
#include "utils/tfcc_cudautils.h"
#endif

int main()
{
#ifdef TFCC_WITH_MKL
    tfcc::initialize_mkl(1,1);
#else
    tfcc::initialize_cuda();
#endif

    tfcc::Variable<float> a({2, 3});
    tfcc::Variable<float> b({2, 3});

    tfcc::data::set(a, {1, 2, 3, 4, 5, 6});
    tfcc::data::set(b, {2, 3, 4, 5, 6, 7});

    tfcc::Variable<float> c = a + b;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl;
    std::cout << "c: " << c << std::endl;
    return 0;
}
