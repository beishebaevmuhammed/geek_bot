import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("bot.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print('DB connected successfully')

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_TABLE_QUERY)
        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
            self.connection.execute(sql_queries.ALTER_USER_V2_TABLE)
            self.connection.execute(sql_queries.ALTER_FIRST_NAME_TABLE)
        except sqlite3.OperationalError:
            pass
        self.connection.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name, None, 0,)
        )
        self.connection.commit()

    def sql_insert_new_ban_user(self, tg_id):
        self.cursor.execute(
            sql_queries.INSERT_NEW_BAN_USER_QUERY,
            (None, tg_id, 1)
        )
        self.connection.commit()

    def sql_select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_ban_user_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_profile(self, tg_id, nickname, biography, age, gender, city, relationship_status, photo):
        self.cursor.execute(
            sql_queries.INSERT_PROFILE_QUERY,
            (None, tg_id, nickname, biography, age, gender, city, relationship_status, photo,)
        )
        self.connection.commit()



    def sql_select_profile(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "age": row[4],
            "gender": row[5],
            "city": row[6],
            "relationship_status": row[7],
            "photo": row[8]
        }
        return self.cursor.execute(
            sql_queries.SELECT_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_select_filter_profiles(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "age": row[4],
            "gender": row[5],
            "city": row[6],
            "relationship_status": row[7],
            "photo": row[8]
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_PROFILE_LIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_update_profile(self, nickname, biography, age, gender, photo, city, relationship_status, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_PROFILE_QUERY,
            (nickname, biography, age, gender, city, relationship_status, photo, tg_id,)
        )
        self.connection.commit()

    def sql_delete_profile(self, tg_id):
        self.cursor.execute(
            sql_queries.DELETE_PROFILE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_update_user_link(self, link, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_LINK_QUERY,
            (link, tg_id,)
        )
        self.connection.commit()

    def sql_select_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
            "balance": row[6],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_reference_menu_data(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
            "total_referral": row[1],
        }
        return self.cursor.execute(
            sql_queries.DOUBLE_SELECT_REFERRAL_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
            "balance": row[6],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_insert_referral(self, owner_id, referral_id, first_name):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner_id, referral_id, first_name)
        )
        self.connection.commit()

    def sql_update_balance(self, owner):
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (owner,)
        )
        self.connection.commit()

    def sql_select_referral(self, referral_first_name):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "owner_telegram_id": row[1],
            "referral_telegram_id": row[2],
            "referral_first_name": row[3],
        }
        return self.cursor.execute(
            sql_queries.SELECT_REFERRAL_QUERY,
            (referral_first_name,)
        ).fetchone()
