from models import *

if __name__ == '__main__':
    with Session(engine) as session:
       first_selection = input('''
What would you like to do?
1. See all Posts
2. Find a Post
3. Create a new post
4. Delete a post
5. Edit a post
              ''')
       
    if first_selection == '1':
        allp = session.query(Post).all()
        print(allp)
    elif first_selection == '2':
        selected_id = input("Please select an ID")
        post = session.query(Post).filter(Post.id == selected_id).first()
        if post:
            print(post)
        else:
            print("Post not found")
    elif first_selection == '3':
        user = input("Please enter a user")
        title = input("Please enter a title")
        content = input("Please enter a content")
        year = input("Please enter a year")
        post = Post(
            user = user,
            title = title,
            content = content,
            year = year
        )
        session.add(post)
        session.commit()

    elif first_selection == '4':
        selected_id = input("Please select an ID to Delete")
        post = session.query(Post).filter(Post.id == selected_id).first()
        if post:
            session.delete(post)
            session.commit()
        else:
            print("Post not found")