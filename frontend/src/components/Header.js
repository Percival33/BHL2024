import React from 'react';

export function Header({ onSearchChange }) {

  return (
      <>
        <nav className="bg-our_dark border-gray-200 mb-5">
          <div className="flex flex-wrap items-left justify-between p-4 mx-40">
            <a href="http://localhost:3000/" className="flex items-left space-x-3 rtl:space-x-reverse">
              <img src="/logo512_our.png" className="h-8" alt="Flowbite Logo" />
              <span className="self-left text-2xl font-semibold whitespace-nowrap text-white">
              SmartNotes
            </span>
            </a>
            <form className="flex md:order-2">
              <button type="button" data-collapse-toggle="navbar-search" aria-controls="navbar-search" aria-expanded="false"
                      className="md:hidden text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5 me-1">
                <svg className="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                  <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                </svg>
                <span className="sr-only">Search</span>
              </button>
              <div className="relative md:block">
                <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                  <svg className="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                  </svg>
                  <span className="sr-only">Search icon</span>
                </div>
                <input type="text" id="search-navbar" className="block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                       placeholder="Search..." onChange={(e) => onSearchChange(e.target.value)} />
              </div>
            </form>
          </div>
        </nav>
      </>
  );
}