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

from tensorflow.python.framework.ops import Operation
import ir.framework
import ir.node
from ..converter import Converter


# implement for https://www.tensorflow.org/api_docs/cc/class/tensorflow/ops/minimum?hl=en
class Minimum(Converter):
    def __call__(self, op: Operation, graph: ir.framework.Graph):
        if not self.accept(op):
            return False

        #print("Converter Minimum: op.inputs={}, op.outputs={}".format(op.inputs,op.outputs))
        inp_strs = [inp.name for inp in op.inputs]
        oup_strs = [oup.name for oup in op.outputs]
        graph.append_node(ir.node.math.Min(op.name, graph, inp_strs, oup_strs))
        return True
