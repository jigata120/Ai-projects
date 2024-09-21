export const getData = async (url = '') => {
  try {
      const response = await fetch(url, {
          method: 'GET',
          headers: {
              'Content-Type': 'application/json',
          },
      });

      if (!response.ok) {
          throw new Error('Response was not ok');
      }

      const result = await response.json();
      console.log(result);

      return result;
  } catch (error) {
      console.error('Error fetching data:', error);
  }
};


export const postData = async (url = '', data = {data:"ex"}) => {
    
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), 
      });
 
      if (!response.ok) {
        throw new Error('Response was not ok');
      }
  
      const result = await response.json(); 
      console.log(result)

      return result;
     
  };

  export const updateData = async (url = '', data = {}) => {
    const response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
  
    if (!response.ok) {
      throw new Error('Response was not ok');
    }
  
    const result = await response.json();
    console.log("updated");
  
    return result;
  };