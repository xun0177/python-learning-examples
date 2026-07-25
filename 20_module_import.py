"""
第20题：模块导入基础
知识点：import 整个模块、from...import 导入指定函数、as 起别名
"""

def module_import_demo():  # 函数名清晰表达"模块导入演示"的功能
    """演示 Python 中导入模块的多种方式"""
    print("=== 模块导入演示 ===")

    # ---------- 方式一：导入整个模块 ----------
    # import 模块名：导入整个模块，使用时需要加模块名前缀
    import math
    # 使用 math. 前缀访问模块中的内容
    print(f"半径为3的圆的面积：{math.pi * 3 ** 2}")  # math.pi 是圆周率

    # ---------- 方式二：只导入需要的函数 ----------
    # from 模块名 import 函数名：直接导入指定函数，使用时不需要前缀
    from math import sqrt  # 只导入 sqrt 函数
    print(f"16的平方根：{sqrt(16)}")  # 直接使用 sqrt()，不需要 math. 前缀

    # ---------- 方式三：导入模块并起别名 ----------
    # import 模块名 as 别名：为模块取一个简短或更易记的名字
    import random as rd  # 将 random 模块简化为 rd
    print(f"掷骰子（1-6随机数）：{rd.randint(1, 6)}")  # 使用别名 rd 调用

    # ---------- 方式四：从模块中导入特定函数 ----------
    # from 模块名 import 函数名：直接导入，使用时无需前缀
    from random import choice  # 导入 choice 函数（从列表中随机选一个元素）
    colors = ["红", "绿", "蓝"]
    print(f"随机颜色：{choice(colors)}")


# 调用函数执行演示
module_import_demo()


"""
补充说明

1. 四种导入方式的对比：

   | 导入方式 | 语法 | 调用方式 | 适用场景 |
   |----------|------|----------|----------|
   | 导入整个模块 | import math | math.pi | 需要使用模块中多个功能时 |
   | 导入指定函数 | from math import sqrt | sqrt(16) | 只需要模块中少数几个函数时 |
   | 导入并起别名 | import random as rd | rd.randint() | 模块名太长或需要简化时 |
   | 导入多个函数 | from math import sqrt, pow | 直接使用 | 同时需要模块中多个特定函数 |

2. 为什么需要模块导入？
   - Python 内置了丰富的标准库（如 math、random、datetime 等），通过导入即可使用。
   - 模块化设计让代码更清晰、可复用。
   - 将不同功能的代码分离到不同模块中，便于维护。

3. 常用导入模式：
   - import 模块名：最常用，明确知道函数来自哪个模块。
   - from 模块名 import 函数名：代码更简洁，但要避免命名冲突。
   - import 模块名 as 别名：适合模块名较长的情况（如 matplotlib.pyplot as plt）。

4. 命名优化说明：
   - 原函数名 exercise_21 改为 module_import_demo（题号修正为20，功能描述更清晰）。
   - 原打印内容增加中文语境，结合 f-string 和更完整的句子表述。

5. 常见标准库模块举例：
   - math：数学函数（三角函数、对数、开方等）
   - random：随机数生成
   - datetime：日期和时间处理
   - os：操作系统接口
   - sys：Python 运行时环境
   - json：JSON 数据处理
   - re：正则表达式

6. 扩展思考：
   - 如何导入自定义模块（自己写的 .py 文件）？
   - 如果导入的两个模块中有同名的函数，会发生什么？（提示：后导入的会覆盖先导入的）
   - __name__ 属性有什么作用？（提示：判断是直接运行还是被导入）
   - 如何查看模块中所有可用的函数和属性？（提示：dir() 函数）
"""