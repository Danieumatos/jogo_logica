// script.js

document.addEventListener('DOMContentLoaded', function() {
    const modoDesafio = document.getElementById('modo-desafio');
    const submenuDificuldade = document.getElementById('submenu-dificuldade');
    const fecharErro = document.getElementById('fechar-erro');
    const fecharDica = document.getElementById('fechar-dica');
    const botaoDica = document.getElementById('botao-dica');

    if (modoDesafio) {
        modoDesafio.addEventListener('click', function(event) {
            event.preventDefault();
            submenuDificuldade.style.display = 'flex';
        });
    }

    if (fecharErro) {
        fecharErro.addEventListener('click', function() {
            document.getElementById('popup').style.display = 'none';
        });
    }

    if (fecharDica) {
        fecharDica.addEventListener('click', function() {
            document.getElementById('dica-popup').style.display = 'none';
        });
    }

    if (botaoDica) {
        botaoDica.addEventListener('click', function() {
            const nivel = this.getAttribute('data-nivel');
            const dificuldade = this.getAttribute('data-dificuldade');
            const url = dificuldade 
                ? `/dica_desafio/${dificuldade}/${nivel}` 
                : `/dica/${nivel}`;
                
            fetch(url)
                .then(response => response.text())
                .then(data => {
                    document.getElementById('dica-texto').innerText = data;
                    document.getElementById('dica-popup').style.display = 'flex';
                })
                .catch(error => console.error('Erro ao buscar a dica:', error));
        });
    }
});
