# Importando a bilbioteca Streamlit
import streamlit as st

# Escrevendo o comando olá mundo para ser exibido no navegador
# st.write("Olá Mundo!")

# Criando uma função jedi
def jedi():
    name = st.text_input("Nome do Jedi: ")
    age = st.number_input("Idade do Jedi: ", value=0, step=1, min_value=0, max_value=1500)
    return name, age

def principal():
    st.title("Jedi App")
    st.subheader("Por favor, informe seus dados abaixo: ")

    name, age = jedi()
    # Criando uma lista suspensa com as categorias de Jedi
    st.write("Selecione a categoria de jedi que você pertence: ")
    category = st.selectbox ("Categoria de Jedi", ("Padawan", "Cavaleiro", "Mestre"))

    # Criando um botão para enviar os dados
    submit = st.button("Enviar dados")

    if submit:
        st.write("Seus dados foram enviados!")
        # Vamo9s exibir uma mensagem com os dados do Jedi
        st.write("O Jedi", name, "da categoria", category, "tem", age, "anos.")

    # Exibe uma imagem no Jedi
    st.image("rey.jpg", width=200)

if __name__ == "__main__":
    principal()