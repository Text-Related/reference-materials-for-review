# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random


class ForestFire(object):

    def __init__(self, cells_shape):
        """
        Parameters
        ----------
        cells_shape : 一个元组，表示画布的大小。
        Examples
        --------
        建立一个高20，宽30的画布
        fire = ForestFire((20, 30))
        
        """

        # 矩阵的四周不参与运算
        self.cells = np.zeros(cells_shape)

        real_width = cells_shape[0] - 2
        real_height = cells_shape[1] - 2
                                 
        # 随机初始化矩阵
        self.cells[1:-1, 1:-1] = np.random.randint(0, 3, size=(real_width, real_height))
        self.timer = 0
    
    def update_state(self, p, f):
        """更新一次状态"""
        buf = np.zeros(self.cells.shape)
        cells = self.cells
        for i in range(1, cells.shape[0] - 1):
            for j in range(1, cells.shape[0] - 1):
                # 正在燃烧的树变成空格位
                if cells[i, j] == 1:
                    buf[i, j] = 0
                # 在空格位，树以概率p生长
                if cells[i, j] == 0:
                    k = random.random()
#                    print("k:", k)
                    if k <= p:
                        buf[i ,j] = 2
                    else:
                        buf[i, j] = 0
                # 在绿树位
                if cells[i, j] == 2:
                    # 计算绿树位周围燃烧的树的个数
                    neighbor = cells[i-1:i+2, j-1:j+2].reshape((-1, ))
                    neighbor_num = neighbor.tolist().count(1)
                    # 如果该细胞周围有正在燃烧的树
                    if neighbor_num != 0:
                        buf[i, j] = 1
                    # 如果该细胞周围没有正在燃烧的树
                    else:
                        t = random.random()
#                        print("t:", t)
#                        print("\n")
                        if t <= f:
                            buf[i, j] = 1
                        else:
                            buf[i, j] = 2
                        
        self.cells = buf
        self.timer += 1
    
    def plot_state(self):
        """画出当前的状态"""
        plt.title('Iter :{}'.format(self.timer))
        plt.imshow(self.cells)
        plt.show()

    def update_and_plot(self, n_iter):
        """更新状态并画图
        Parameters
        ----------
        n_iter : 更新的轮数
        """
        plt.ion()
        for _ in range(n_iter):
            plt.title('Iter :{}'.format(self.timer))
            plt.imshow(self.cells)
            self.update_state(0.1, 0.00006)
            plt.pause(0.01)
        plt.ioff()
                    

if __name__ == '__main__':
    fire = ForestFire(cells_shape=(60, 60))
    fire.update_and_plot(200)

