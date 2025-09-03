from django.db import models

class Peca(models.Model):
    descricao = models.CharField(max_length=200, verbose_name='Descrição da Peça')
    fornecedor = models.CharField(max_length=100, verbose_name='Fornecedor')

    endereco_rua = models.CharField(max_length=200, verbose_name='Rua', blank=True)
    endereco_numero = models.CharField(max_length=20, verbose_name='Número', blank=True)
    endereco_complemento = models.CharField(max_length=100, verbose_name='Complemento', blank=True)
    endereco_bairro = models.CharField(max_length=100, verbose_name='Bairro', blank=True)
    endereco_cidade = models.CharField(max_length=100, verbose_name='Cidade', blank=True)
    endereco_estado = models.CharField(max_length=2, verbose_name='Estado', blank=True,
                                      choices=(
                                          ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
                                          ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
                                          ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
                                          ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
                                          ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
                                          ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
                                          ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
                                          ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
                                          ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
                                          ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
                                      ))
    endereco_cep = models.CharField(max_length=10, verbose_name='CEP', blank=True)
    
    telefone_fornecedor = models.CharField(max_length=20, verbose_name='Telefone do Fornecedor')
    marca = models.CharField(max_length=100, verbose_name='Marca da Peça')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro', null=True, blank=True)
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização', null=True, blank=True)

    class Meta:
        verbose_name = 'Peça'
        verbose_name_plural = 'Peças'
        ordering = ['-data_cadastro']

    def endereco_completo(self):
        parts = [
            f"{self.endereco_rua}, {self.endereco_numero}" if self.endereco_numero else self.endereco_rua,
            self.endereco_complemento,
            self.endereco_bairro,
            f"{self.endereco_cidade} - {self.endereco_estado}",
            f"CEP: {self.endereco_cep}"
        ]
        return ", ".join([part for part in parts if part])
    
    def __str__(self):
        return f"{self.descricao} - {self.marca}"