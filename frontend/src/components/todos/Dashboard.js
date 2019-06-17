import React from 'react';
import TodoCreate from './TodoCreate';
import TodoList from './TodoList';

function Dashboard() {
  return (
    <div className='ui container'>
      <TodoCreate />
      <TodoList />
    </div>
  );
}

export default Dashboard;
