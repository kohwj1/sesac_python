from sqlalchemy import create_engine, Integer, String, Column, select
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///users.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)

def create_user(sess, name:str, age:int) -> User:
    new_user = User(name=name, age=age)
    sess.add(new_user)
    sess.commit()
    return new_user

def get_list(sess):
    return sess.query(User).all()

def get_user_by_id(sess, user_id) -> User | None:
    result = sess.get(User, user_id)
    return result

def update_user_age(sess, user_id, new_age):
    user = sess.get(User, user_id)
    if not user:
        return False
    user.age = new_age
    sess.commit()
    return True;


def delete_user_by_id(sess, user_id):
    user = sess.get(User, user_id)
    if not user:
        return False
    sess.delete(user)
    sess.commit()
    return True;

def delete_user_by_name(sess, user_name) -> int:
    users = sess.query(User).filter_by(name=user_name).all()
    for u in users:
        sess.delete(u)
    sess.commit()
    return len(users);


if __name__ == '__main__':
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    with Session() as sess:
        #사용자 조회
        alice = create_user(sess, 'Alice', 30)
        bob = create_user(sess, 'Bob', 5)
        print(f'추가된 유저: {alice.id}, {bob.id}')

        #사용자 조회
        user1 = get_user_by_id(sess, alice.id)
        print(f'조회한 사용자 정보: {user1.name, user1.age}')

        user2 = get_user_by_id(sess, bob.id)
        print(f'조회한 사용자 정보: {user2.name, user2.age}')

        #정보 수정
        update_alice = update_user_age(sess, alice.id, 29)
        print(f'업데이트 성공 여부: {update_alice}')

        #전체 사용자 조회
        users = get_list(sess)
        for u in users:
            print(f'아이디: {u.id}, 이름: {u.name}, 나이: {u.age}')

        #사용자 삭제
        delete_alice = delete_user_by_name(sess, 'Alice')
        print(f'앨리스 삭제 개수: {delete_alice}')

        #최종 사용자 조회
        users = get_list(sess)
        for u in users:
            print(f'아이디: {u.id}, 이름: {u.name}, 나이: {u.age}')