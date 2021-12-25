function showToast(message) {
nativeToast({
    message: "Message",
    position: 'north',    
    rounded: true,
    timeout: 2000,
    type: 'none',
    icon: false,
    edge:true,
    closeOnClick: true,
    elements: [createElement()]
  })
}

function createElement(){
    let el = document.createElement('div');
    //let child = document.createElement('input');
    //el.appendChild(child);
    return el;
}