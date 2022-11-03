import React, { useEffect } from 'react';

const Modal = ({closeModal, modalContent}) => {
  // use use effect to close the modal
  useEffect(()=> {
    setTimeout(() => {
      closeModal();
    }, 3000);
  });
  return (
    <div className='modal'>
      <p>{modalContent}</p>
    </div>
  );
};

export default Modal;
