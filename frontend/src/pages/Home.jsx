import Navbar from '../components/Navbar'
const Home = () => {
  return (
    <>
      <Navbar />
      <div className="container">
        <div className="row">
          <h1>CLT vs PJ</h1>
            <form>
                <div className="mb-3">
                    <input type="text" className="form-control" id="clt" placeholder="Salario CLT" />
                </div>
                <div className="mb-3">
                    <input type="text" className="form-control" id="subject-matter" placeholder="Salario PJ" />
                </div>
                <button type="submit" className="btn btn-primary">Calcular</button>
            </form>
        </div>
    </div>
    </>
  )
}

export default Home;
