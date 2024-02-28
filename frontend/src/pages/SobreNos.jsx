import { useState } from 'react'

function SobreNos() {
  const [count, setCount] = useState(0)

  return (
    <>
      <header class="bg-dark py-5">
        <div class="container px-4 px-lg-5 my-5">
          <div class="text-center text-white">
            <h1 class="display-4 fw-bolder">Sobre nós</h1>
            <p class="lead fw-normal text-white-50 mb-0">Aprenda um pouco mais sobre nossa loja :)</p>
          </div>
        </div>
      </header>

      <h1>Sobre nós ...</h1>
    </>
  )
}

export default SobreNos