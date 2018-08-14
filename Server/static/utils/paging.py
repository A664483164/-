#! /usr/bin/env.python
# -*- coding:utf-8 -*-
# __author__ = 'CharmNight'
# Date: 2018/4/4

"""分页工具"""


class Paging:

    def __init__(self, page_now, data, page_nub=5, page_index=13):
        """
        初始化数据
        :param page_now:    当前页数
        :param data:        总数据
        :param page_nub:    分页最多显示多少个标签
        :param page_index:  每页展示多少数据
        """
        # 分页
        self.page_index = page_index  # 每页显示的条数
        self.page_nub = page_nub  # 分页标签有多少个
        self.data = data  # 所有数据
        self.data_count = len(self.data)  # 数据总量
        self.show_data = None

        self.half_nub = self.page_nub // 2  # 一半的标签个数

        page_count, mod = divmod(self.data_count, self.page_index)
        self.page_count = page_count + 1 if mod else page_count  # 计算总页数

        try:
            self.page_now = int(page_now)  # 当前页
        except TypeError:
            self.page_now = 1
        if self.page_now > self.page_count:
            self.page_now = self.page_count
        elif self.page_now <= 0:
            self.page_now = 1

    @property
    def start(self):
        """起始数据位置"""
        return (self.page_now - 1) * self.page_index  # 数据开始

    @property
    def end(self):
        """数据结束位置"""
        return self.page_now * self.page_index  # 数据结束位置

    def home_page(self):
        """首页"""
        return 1

    def trailer_page(self):
        """尾页"""
        return self.page_count

    def has_previous(self):
        """是否有上一页"""
        if (self.page_now - 1) <= 0:
            return False
        return True

    def has_next(self):
        """是否有下一页"""
        if (self.page_now + 1) > self.page_count:
            return False
        return True

    def previous_page(self):
        """上一页页数"""
        if self.has_previous():
            return self.page_now - 1
        return self.page_now

    def next_page(self):
        """下一页页数"""
        if self.has_next():
            return self.page_now + 1
        return self.page_now

    def display_data(self):
        """展示数据"""
        self.show_data = self.data[self.start: self.end]
        return self.show_data

    def show_page(self):
        """展示分页"""
        if self.page_count > self.page_index:
            if self.page_now <= self.half_nub:
                # 如果当前页数小于 半数的显示页数则显示前
                ret = [page for page in range(1, self.page_nub + 1)]
            elif self.page_now + self.half_nub > self.page_count:
                ret = [page for page in range(self.page_count - self.page_nub + 1, self.page_count + 1)]
            else:
                ret = [i for i in range(self.page_now - self.half_nub, self.half_nub + self.page_now + 1)]
            return ret
        else:
            return [i for i in range(1, self.page_count + 1)]