
import Navbar from "./Navbar"

function Layout({children}) {
    return (
        <>
            <Navbar />
            {/* {% if messages %}
            {% for message in messages %}
            <div class="alert alert-warning alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            {% endfor %}
            {% endif %} */}

            {children}

            <footer class="py-5 bg-dark">
                <div class="container"><p class="m-0 text-center text-white">Copyright &copy; Your Website 2023</p></div>
            </footer>
          
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
            
            <script src="{% static 'js/scripts.js' %}"></script>
        </>
    )
}

export default Layout