// SPDX License Identifier: MIT

pragma solidity >0.4.0;

contract anac{
    // variável que armazena a idade
    uint public idade;
    // variável que armazena o dono do contrato
    address private owner;

    constructor() {
        // Define o owner
        owner = msg.sender;
        
        // Idade padrão
        idade = 18;
    }

    // Função que verifica se quem está chamando é o dono do contrato
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    // Função que recebe o valor da idade e atribui a variável idade
    // Apenas o dono do contrato pode chamar essa função
    function setIdade (uint256 novaIdade) public onlyOwner() {
        idade = novaIdade;
    }
    
    // Função que retorna a idade
    function getIdade() public view returns (uint256) {
        return idade;
    }
}
