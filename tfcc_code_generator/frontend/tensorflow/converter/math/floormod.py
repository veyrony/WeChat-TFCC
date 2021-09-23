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

import logging

class FloorMod(Converter):
    def __call__(self, op: Operation, graph: ir.framework.Graph):
        if not self.accept(op):
            #logging.debug("FloorMod accept error, self.optype={}, input.optype={}".format(self.op_type, op.type))
            return False

        inp_strs = [inp.name for inp in op.inputs]
        oup_strs = [oup.name for oup in op.outputs]
        assert len(inp_strs) == 2 and len(oup_strs) == 1


        graph.append_node(ir.node.math.Div(op.name, graph, inp_strs, oup_strs))
        return True

        # a mod b is equal to a - a/b*b
        a_name = inp_strs[0]
        b_name = inp_strs[1]

        a_div_b_out_name = graph.context.create_symbol_name(a_name + "_d_" + b_name)
        graph.append_node(
                ir.node.math.Div(op.name + ":div", graph, [a_name, b_name], [a_div_b_out_name])
        )

        a_div_b_mul_b_out_name = graph.context.create_symbol_name(a_name + "_d_" + b_name + "_m_" + b_name)
        graph.append_node(
                ir.node.math.Div(op.name + ":mul", graph, [a_div_b_out_name, b_name], [a_div_b_mul_b_out_name])
        )

        # debug
        for inp in inp_strs:
            s = graph.get_symbol(inp)
            logging.debug("FloorMod input name {}, type {}".format(s.name, s.dtype))


        graph.append_node(ir.node.math.Sub(op.name, graph, [a_name, a_div_b_mul_b_out_name], oup_strs))
        return True
