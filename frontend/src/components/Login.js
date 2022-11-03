import React, { useRef } from 'react';
import kefisApis from '../utils/apiService/api';
import { setToken } from '../utils/apiService/helpers';


const LoginPage = ({onSubmit}) => {
    const emailRef = useRef();
    const passwordRef = useRef();

    const loginUser = async (data) => {
      try {
        const { data: response } = await kefisApis.login(data);
        console.log(response);
        setToken(response.access.access_token);
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
        <h5 >Login to continue ... </h5>
      </span>
    </div>
      <form onSubmit={handleSubmit} className='form'>
        <div className='form-control'>
          <label for="email">Email</label>
          <input
            type="text"
            name="email"
            ref={emailRef}
          />
        </div>
        <div className='form-control'>
          <label for="password">Password</label>
          <input
            type="password"
            name="password"
            ref={passwordRef}
          />
        </div>
        <button className='btm' type="submit" color="primary">login</button>
      </form>
    </>
  );
}

export default LoginPage;