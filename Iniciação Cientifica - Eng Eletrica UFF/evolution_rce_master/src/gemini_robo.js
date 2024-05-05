const { GoogleGenerativeAI } = require("@google/generative-ai");




class GeminiCardapio {
    constructor() {
        this.cardapio = {
            "cafe": {
                "description": "Café preto",
                "price": 2.5
            },
            "pao": {
                "description": "Pão francês",
                "price": 1.5
            },
            "misto": {
                "description": "Misto quente",
                "price": 3.5
            },
            "suco": {
                "description": "Suco de laranja",
                "price": 4.0
            }
        }
        this.genAI = new GoogleGenerativeAI(process.env.API_KEY);

    }

    async assistentePedido(msg) {
        const model = this.genAI.getGenerativeModel({ model: "gemini-pro" });
        const chat = model.startChat({
            history: [
                {
                    role: "user",
                    parts: [{ text: "Hello, I have 2 dogs in my house." }],
                },
                {
                    role: "model",
                    parts: [{ text: "Ola, sou seu robo assistente de pizzaria! Meu objetivo é ajudar no seu pedido, esclarecer duvidas e outras funcionalidades de delivery!" }],
                },
            ],
            generationConfig: {
                maxOutputTokens: 100,
            },
        });


        const result = await chat.sendMessage(msg);
        const response = await result.response;
        const text = response.text();
        console.log(text);
    }

    getCardapio() {
        return this.cardapio;
    }

    getPreco(item) {
        return this.cardapio[item].price;
    }

    getDescricao(item) {
        return this.cardapio[item].description;
    }
}