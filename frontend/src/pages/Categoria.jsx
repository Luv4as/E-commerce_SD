import { useState } from "react";

function Categoria() {

    const produto = {}

    return (
        <>
            <header class="bg-dark py-5">
                <div class="container px-4 px-lg-5 my-5">
                    <div class="text-center text-white">
                        <h1 class="display-4 fw-bolder">{{ categoria }}</h1>
                        <p class="lead fw-normal text-white-50 mb-0">Todos nossos produtos da categoria {{ categoria }}</p>
                    </div>
                </div>
            </header>
            
            <section class="py-5">
                <div class="container px-4 px-lg-5 mt-5">
                    <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">

                        {/* {% for produto in produtos %}
                        {% if produto.e_saldo %} */}

                        <div class="col mb-5">
                            <div class="card h-100">
                               
                                <div class="badge bg-dark text-white position-absolute"
                                    style={{top: '0.5rem', right: '0.5rem'}}>SALDO</div>

                                
                                <img class="card-img-top" src="{{ produto.imagem.url }}" alt="..." />
                               
                                <div class="card-body p-4">
                                    <div class="text-center">
                                       
                                        <h5 class="fw-bolder"> produto.nome </h5>
                                        <strike>R$ produto.preco </strike>
                                        <br />
                                        R$ produto.preco_saldo 
                                        <br />
                                        produto.descricao 
                                    </div>
                                </div>
                             
                                <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                    <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="{% url 'produto' produto.id %}">Ver produto</a></div>
                                </div>
                            </div>
                        </div>

                        {/* {% else %} */}
                        <div class="col mb-5">
                            <div class="card h-100">
                               
                                <img class="card-img-top" src="{{ produto.imagem.url }}" alt="..." />
                               
                                <div class="card-body p-4">
                                    <div class="text-center">
                                       
                                        <h5 class="fw-bolder"> produto.nome </h5>
                                        
                                        R$ produto.preco 
                                        <br />
                                        produto.descricao 
                                    </div>
                                </div>
                                
                                <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                    <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="{% url 'produto' produto.id %}">Ver produto</a></div>
                                </div>
                            </div>
                        </div>
                        {/* {% endif %}
                        {% endfor %} */}

                    </div>
                </div>
            </section>             
        </>
    )
}

export default Categoria