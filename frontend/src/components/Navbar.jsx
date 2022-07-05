import ellunLogo from '../assets/images/ellun-logo.png'

const Navbar = () => {
    return(
        <nav className="navbar">
            <img src={ellunLogo}
              width="120px" height="57.2px" alt="Evolute Contabilidade" />
        </nav>
    )
}

export default Navbar;
