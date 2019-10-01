#!/usr/bin/env python
# coding: utf-8


class VKPoster:

    def __init__(self):
        self.pp = dict()
        self.pr = dict()
        self.pf = dict()

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        self.pp.setdefault(user_id, [])
        self.pp[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        self.pr.setdefault(post_id, [])
        self.pr[post_id].append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        self.pf.setdefault(follower_user_id, [])
        self.pf[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        s = self.pf[user_id]
        for i in range(len(s)):
            for k1, v in self.pp.items():
                if s[i] == k1:
                    l1 = self.pp[s[i]]
                    for j in range(len(l1)):
                        q.append(l1[j])
        q = sorted(q, reverse=True)
        return q[:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        kd = {}
        ks = []
        for key in self.pr:
            self.pr[key] = list(set(self.pr[key]))
            s = len(self.pr[key])
            kd.setdefault(key, s)
        t_list = list(kd.items())
        t_list.sort(key=lambda elem: elem[0], reverse=True)
        t_list.sort(key=lambda elem: elem[1], reverse=True)
        for i in range(len(t_list)):
            ks.append(t_list[i][0])
        return ks[:k]
