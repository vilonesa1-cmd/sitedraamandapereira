# Dra. Amanda Pereira — landing page (prévia)

Página única com CSS, JavaScript, imagens e logo embutidos. Não precisa de build nem de dependências.

## Estrutura
- `index.html`: o site (versão atual). Abra no navegador ou publique esta pasta em qualquer hospedagem estática (Vercel, Netlify, GitHub Pages).
- `imagens/`: fotos originais usadas (antes e depois, retrato) e o vídeo de referência do efeito do comparador.
- `docs/`: avaliações do Google e os prompts-mestre usados como base.
- `fonte/build_estelar.py`: script que gera o `index.html` (usa PIL para cortar as fotos de antes e depois). Os caminhos dentro dele apontam para o ambiente em que foi criado; ajuste-os se for rodar de novo.
- `fonte/previa-primeira-versao.html`: primeira prévia, anterior à versão baseada no site de referência.

## Pendências (a finalizar depois que a cliente fechar)
- Fotos reais do Instagram (lista `POSTS` no final do `index.html`)
- Fotos do consultório (seção "Um espaço pensado para o seu conforto")
- Autorização de antes e depois e avaliações, conforme regras do CRBM
- Domínio final (og:image, canonical, robots e sitemap)
