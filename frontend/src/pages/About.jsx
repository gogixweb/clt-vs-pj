import Navbar from '../components/Navbar';
import william from '../assets/images/devs/william-ribeiro.jpeg';
import linkedinLogo from '../assets/images/linkedin.png';
import githubLogo from '../assets/images/github.png';


const About = () => {

  return(
    <>
      <Navbar />

      <div className='container'>
        <div className='row'>
            <div>
                <h3>Desenvolvido com &#10084; por: </h3>
            </div>
        </div>

        <div className='row'>
          <div className='col-md-3'>
              <div className='card card-size'>
                  <img src={william} className='card-img-top' alt='...' width='250px' height='250px'/>
                  <div className='card-body'>
                      <h5 className='card-title'>William Ribeiro</h5>
                      <p className='card-text'>
                          <i>'Eu não sou lá muito bom com Frontend, mas dou meus pulos'</i>
                      </p>
                      <div className='text-center'>
                          <a
                            target='_blank'
                            href='https://www.linkedin.com/in/williamlimaribeiro/'
                            rel='nooper noreferrer'
                          >
                            <img className='mini-logo' src={linkedinLogo} alt='linkedin logo'/>
                          </a>
                          <a target='_blank' href='https://github.com/wlribeiro' rel='noreferrer'>
                            <img className='mini-logo' src={githubLogo} alt='github logo'/>
                          </a>
                      </div>
                  </div>
              </div>
          </div>
        </div>
        
      </div>
    </>
  )
}

export default About;
