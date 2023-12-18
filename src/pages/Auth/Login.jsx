import background from '../../assets/valeriia-bugaiova.png'
import logo from '../../assets/logo.png'
import Form from 'react-bootstrap/Form';

const LoginPage = () =>{
    return (
    <div className="App w-100 min-vh-100">
        <div className="absolute text-white min-vh-100 d-flex align-items-center justify-content-center" style={{zIndex: '10'}}>
            <div className='card p-5' style={{width:'35%'}}>
                <div className='col'>
                    <div className='row d-flex justify-content-center align-items-center'>
                        <img src={logo} style={{
                            width:'25%',
                            }} 
                            alt="logo" />
                        <h5 className='text-center my-2'>Login</h5>
                    </div>
                    <div className='row'>
                        <div className='col'>
                            <Form>
                                <Form.Group className="mb-3" controlId="formBasicUser">
                                    <Form.Label>Username</Form.Label>
                                    <Form.Control size="sm" type="user" placeholder="Enter username" />
                                </Form.Group>
                                <Form.Group className="mb-3" controlId="formBasicPassword">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control size="sm" type="password" placeholder="Password" />
                                </Form.Group>
                                <div className='w-100 d-flex justify-content-between'>
                                    <p>
                                        Belum punya akun?
                                        <a href="/register" className='text-decoration-none text-primary'> Register</a>
                                    </p>
                                    <a href="#Lupa" className='text-danger text-decoration-none'>
                                        Lupa kata sandi?
                                    </a>
                                </div>
                                <div className='row'>
                                    <div className='col'>
                                        <button className='btn w-100'
                                            style={{
                                                backgroundColor:'#63B0DB',
                                                }} 
                                        >Login</button>
                                    </div>
                                </div>
                            </Form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <img src={background} style={{
            minWidth: '1024px',
            maxHeight: '100%',
            width: '100%',
            height: 'auto',
            position: 'fixed',
            top: 0,
            left: 0,
            objectFit: 'cover',
            zIndex: '-1'
            }} 
            alt="logo" />
    </div>
    );
  }

export default LoginPage;