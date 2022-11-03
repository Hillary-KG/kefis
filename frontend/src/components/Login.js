import React, { useRef } from 'react';;


const LoginPage = ({onSubmit}) => {
    const emailRef = useRef();
    const passwordRef = useRef();

    const handleSubmit = (e) => {
    e.preventDefault();
    const data = {
        email: emailRef.current.value,
        password: passwordRef.current.value
    };
    onSubmit(data);
  }
    return (
    <>
    <div>
      <span>
        <h5>Login to continue ... </h5>
      </span>
    </div>
      <form onSubmit={handleSubmit} className='form'>
        <div>
          <input
            type="text"
            name="email"
            ref={emailRef}
          />
        </div>
        <div>
          <input
            type="password"
            name="password"
            ref={passwordRef}
          />
        </div>
        <button className='submit'>login</button>
      </form>
    </>
  );
}

export default LoginPage;