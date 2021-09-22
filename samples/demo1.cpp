#include <iostream>

#include "tfcc.h"
#define TFCC_WITH_MKL 1
#ifdef TFCC_WITH_MKL
#include "utils/tfcc_mklutils.h"
#else
#include "utils/tfcc_cudautils.h"
#endif

int main(int argc, char* argv[])
{
#ifdef TFCC_WITH_MKL
    tfcc::initialize_mkl(1, 1);
#else
    tfcc::initialize_cuda();
#endif

    if (argc < 2)
    {
        std::cout << "Usage: " << argv[0] << " [model_path]" << std::endl;
        return 1;
    }
    tfcc::NPZDataLoader loader(argv[1]);
    tfcc::DataLoader::setGlobalDefault(&loader);

    tfcc::Variable<float> a({2, 3});
    tfcc::data::set(a, {1, 2, 3, 4, 5, 6});

    tfcc::Variable<float> result;
    {
        auto scope1 = tfcc::Scope::scope("scope1");
        tfcc::Constant<float>& b = tfcc::Constant<float>::getConstant("b");
        result = a + b;
        auto scope3 = tfcc::Scope::scope("scope3");
        tfcc::Constant<float>& d = tfcc::Constant<float>::getConstant("d");
        result = result * d;
    }

    {
        auto scope2 = tfcc::Scope::scope("scope2");
        tfcc::Constant<float>& c = tfcc::Constant<float>::getConstant("c");
        result = result - c;
    }

    std::cout << "a: " << a << std::endl;
    std::cout << "result: " << result << std::endl;
    return 0;
}
