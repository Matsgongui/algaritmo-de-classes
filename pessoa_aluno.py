from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, cpf: str):
        self.id = id
        self.nome = nome
        self.__cpf = cpf

    @abstractmethod
    def marcarPresenca(self):
        pass

    def matricular(self):
        print(f"{self.nome} foi matriculado(a).")
class Aluno(Pessoa):
    def __init__(self, id: int, nome: str, cpf: str, matricula: str):
        super().__init__(id, nome, cpf)
        self.__matricula = matricula 
    def set_matricula(self, nova_matricula: str):
        self.__matricula = nova_matricula
      
    def get_matricula(self) -> str:
        return self.__matricula

    def marcarPresenca(self):
        print(f"Aluno {self.nome} marcou presença.")
      
    def matricular(self):
        print(f"Aluno {self.nome} com matrícula {self.__matricula} foi matriculado.")

def main():
    aluno1 = Aluno(id=1, nome="Matheus", cpf="123.456.789-00", matricula="20250001")
    aluno1.marcarPresenca()
    aluno1.matricular()
    
    print("Matrícula atual:", aluno1.get_matricula())
    aluno1.set_matricula("20250002")
    print("Matrícula atualizada:", aluno1.get_matricula())

if __name__ == "__main__":
    main()
