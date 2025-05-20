# 📚 Projeto de Orientação a Objetos: Pessoa e Aluno

Este projeto em Python implementa um diagrama de classes com **herança**, **abstração**, **encapsulamento** e **polimorfismo**, conforme especificações de exercício.

---

## ✅ Requisitos atendidos:

- ✅ A classe `Pessoa` é abstrata
- ✅ O método `marcarPresenca()` é abstrato
- ✅ O atributo `cpf` é **privado**
- ✅ O atributo `matricula` é **fortemente privado**
- ✅ Implementados métodos **acessor (getter)** e **modificador (setter)** para `matricula`
- ✅ Método `main()` criado para testar a classe `Aluno`

---

## 📄 Estrutura

- `Pessoa`: Classe abstrata com atributos `id`, `nome` e `cpf`
- `Aluno`: Herda de `Pessoa` e implementa `matricula`, com seus getters e setters
- O método `matricular()` foi sobrescrito na classe `Aluno`

---

## ▶️ Como executar

1. Salve o código no arquivo `pessoa_aluno.py`
2. Abra um terminal na pasta onde o arquivo está salvo
3. Execute:

```bash
python pessoa_aluno.py
