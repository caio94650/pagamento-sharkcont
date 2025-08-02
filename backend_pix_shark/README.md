
# Backend Pix - Shark Contingências

Este backend permite gerar cobranças via Pix utilizando a API da Pagar.me (Stone).

### 🚀 Como rodar no Railway:

1. Crie um repositório no GitHub e envie estes arquivos.
2. Acesse https://railway.app
3. Clique em **New Project > Deploy from GitHub Repo**
4. Escolha seu repositório
5. O Railway irá detectar automaticamente o `Procfile` e subir o projeto
6. Pegue a URL gerada (ex: `https://seubot.up.railway.app/pix`)

### 🔐 Variáveis (fixas neste projeto)
- `PAGARME_API_KEY`: Sua chave secreta da Stone (já inserida no código — pode trocar depois)

---

### ✅ Endpoint POST /pix

**Exemplo de payload:**

```
{
  "amount": 1000,
  "name": "João Exemplo",
  "email": "joao@email.com",
  "cpf": "12345678900",
  "item": "Proxy Brasil IPv4 7d"
}
```

**Resposta:**

```json
{
  "pixCode": "000201....",
  "qrUrl": "https://...",
  "transactionId": "ord_xyz123"
}
```
