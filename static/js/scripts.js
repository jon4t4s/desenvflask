// Validação de Login (CPF e Senha)
function validarLogin() {
    const cpf = document.getElementById('cpf').value.trim();
    const senha = document.getElementById('senha').value;

    // Verifica CPF (somente se está preenchido)
    if (!cpf) {
        alert('Por favor, insira seu CPF.');
        return false;
    }

    // Verifica senha
    const regexSenha = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$/;
    if (!regexSenha.test(senha)) {
        alert('A senha deve conter no mínimo 6 caracteres, 1 letra maiúscula, 1 número e 1 caractere especial.');
        return false;
    }

    return true; // CPF e senha válidos
}
