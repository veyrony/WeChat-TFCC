# Copyright 2021 Wechat Group, Tencent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def get_all_node_generators():
    from .abs import Abs
    from .argmax import ArgMax
    from .add import Add
    from .sub import Sub
    from .mul import Mul
    from .div import Div
    from .clip import Clip
    from .erf import Erf
    from .gelu import Gelu
    from .leakyrelu import LeakyRelu
    from .matmul import Matmul
    from .matmulwithbias import MatmulWithBias
    from .max import Max
    from .min import Min
    from .mod import Mod
    from .pow import Pow
    from .reduce import ReduceMean, ReduceSum, ReduceProd, ReduceMax, ReduceMin
    from .relu import Relu
    from .rsqrt import Rsqrt
    from .sigmoid import Sigmoid
    from .sign import Sign
    from .softmax import Softmax
    from .sqrt import Sqrt
    from .tanh import Tanh
    from .neg import Neg
    from .reciprocal import Reciprocal
    from .log import Log
    from .softplus import Softplus
    from .topk import TopK

    return [
        Abs,
        ArgMax,
        Add,
        Sub,
        Mul,
        Div,
        Clip,
        Erf,
        Gelu,
        LeakyRelu,
        Matmul,
        MatmulWithBias,
        Max,
        Min,
        Mod,
        Pow,
        ReduceMean,
        ReduceSum,
        ReduceProd,
        ReduceMax,
        ReduceMin,
        Relu,
        Rsqrt,
        Sign,
        Sigmoid,
        Softmax,
        Sqrt,
        Tanh,
        Neg,
        Reciprocal,
        Log,
        Softplus,
        TopK,
    ]
