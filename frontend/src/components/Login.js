import React, { useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import kefisApis from '../utils/api/api';
import { setAuth } from '../utils/helpers/auth-helpers';


const LoginPage = ({onSubmit}) => {
    const emailRef = useRef();
    const passwordRef = useRef();
    const navigate = useNavigate();

    const loginUser = async (data) => {
      try {
        const { data: response } = await kefisApis.login(data);
        const user_type = response.user_type
        setAuth({token: response.access.access_token, user_type });
        switch (user_type) {
          case 0:
            navigate('/orders');
            break;
          case 1:
            navigate('/warehouse');
            break;
          case 2:
            navigate('/retail');
            break;
          default:
            navigate('/login')
            break;
        }
        navigate('/')
      } catch (error) {
        console.log(error);
      }
    }

    const handleSubmit = (e) => {
      e.preventDefault();
      const data = {
          email: emailRef.current.value,
          password: passwordRef.current.value
      };
      loginUser(data);
  }
    return (
    <>
    <div>
      <span className='item'>
        <h5>Login to continue ... </h5>
      </span>
    </div>
      <form onSubmit={handleSubmit} className='form'>
        <div className='form-control'>
          <label htmlFor="email">Email</label>
          <input
            type="text"
            name="email"
            ref={emailRef}
            autoComplete='off'
            required
          />
        </div>
        <div className='form-control'>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            ref={passwordRef}
            required
            autoComplete='off'
          />
        </div>
        <button className='btm' type="submit" color="primary">login</button>
      </form>
    </>
  );
}

export default LoginPage;