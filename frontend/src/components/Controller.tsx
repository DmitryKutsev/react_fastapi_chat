import { useState } from 'react';
import Title from './Title'
import { Textarea } from '@chakra-ui/react';


// const [messages, setMessages] = useState<any[]>([]);


function Controller() {
  return ( 
      <div className="h-screen overflow-y-hidden">
        <Title />
        <div className="flex flex-col justify-between">
          <div className="text-6xl">Hello Controller</div>
          <div className="fixed w-full bottom-0">
          <textarea
              className="resize-none flex justify-between w-full border rounded-md p-2 bg-gray-400 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your text here..."
          />
            {/* <input className="textarea flex justify-between w-full p-5 bg-gray-400 text-white font-bold shadow" name="input" type="text" placeholder="Enter Date"/> */}
          </div>
        </div>
      </div>
  )
}

export default Controller

