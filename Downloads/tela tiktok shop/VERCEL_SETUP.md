# Configuração Vercel - IMPORTANTE

## ⚠️ Problema Identificado

Os arquivos do projeto estão no subdiretório `Downloads/tela tiktok shop/` dentro do repositório Git.

## ✅ Solução

No painel da Vercel, você precisa configurar o **Root Directory**:

1. Acesse o projeto na Vercel
2. Vá em **Settings** → **General**
3. Role até a seção **Root Directory**
4. Configure como: `Downloads/tela tiktok shop`
5. Clique em **Save**
6. Faça um novo deploy

## Configurações de Build

As seguintes configurações já estão no `vercel.json`:
- Build Command: `npm run build`
- Output Directory: `dist`
- Framework: `vite`

## Alternativa

Se preferir, você pode mover os arquivos para a raiz do repositório Git, mas isso requer reorganizar o repositório.

