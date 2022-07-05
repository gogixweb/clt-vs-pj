import image404 from '../assets/images/error-404.png';
import Navbar from '../components/Navbar';

const Page404 = ()  => {
  return (
    <>
    <Navbar />
      <div className='container-404'>
        <img className='image-bounce' src={image404} alt='logo error 404' />
        <h2 className='title-404'>
          Oops, pagina não encontrada
        </h2>
      </div>
    </>

  );
}

export default Page404;
