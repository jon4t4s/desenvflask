document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const senha1 = document.getElementById("senha1");
    const senha2 = document.getElementById("senha2");

    form.addEventListener("submit", function (event) {
        const senha = senha1.value;

        // Requisitos de validação
        const temMaiuscula = /[A-Z]/.test(senha);
        const temNumero = /[0-9]/.test(senha);
        const temEspecial = /[!@#$%^&*(),.?":{}|<>]/.test(senha);
        const comprimentoMinimo = senha.length >= 6;

        // Validações
        if (senha1.value !== senha2.value) {
            event.preventDefault();
            alert("As senhas não coincidem! Por favor, corrija e tente novamente.");
        } else if (!comprimentoMinimo) {
            event.preventDefault();
            alert("A senha deve ter no mínimo 6 caracteres.");
        } else if (!temMaiuscula) {
            event.preventDefault();
            alert("A senha deve incluir pelo menos uma letra maiúscula.");
        } else if (!temNumero) {
            event.preventDefault();
            alert("A senha deve incluir pelo menos um número.");
        } else if (!temEspecial) {
            event.preventDefault();
            alert("A senha deve incluir pelo menos um caractere especial.");
        }
    });
});
