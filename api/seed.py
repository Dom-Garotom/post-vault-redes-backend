from .models import Post

def run():
    print("Limpando posts existentes...")
    Post.objects.all().delete()

    print("Inserindo posts mockados...")

    posts = [
        {
            "userId": 1,
            "title": "Como aprender Django",
            "body": "Primeiro instale o Django, depois crie seu primeiro projeto."
        },
        {
            "userId": 1,
            "title": "Explorando o React",
            "body": "React é uma biblioteca JavaScript para criar interfaces de usuário."
        },
        {
            "userId": 2,
            "title": "UV: O novo gerenciador de pacotes Python",
            "body": "UV é rápido e moderno, ideal para ambientes virtuais leves."
        },
        {
            "userId": 3,
            "title": "Docker para iniciantes",
            "body": "Containerize seu app com facilidade e segurança."
        },
        {
            "userId": 4,
            "title": "Testes em Python",
            "body": "Use Pytest ou Unittest para garantir a qualidade do seu código."
        }
    ]

    for post_data in posts:
        Post.objects.create(**post_data)

    print(f"{len(posts)} posts inseridos com sucesso.")
