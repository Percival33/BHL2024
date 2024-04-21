export function Footer() {

  return (
    <footer
      className="bottom-0 left-0 z-20 w-full p-4 bg-our_dark border-t shadow md:flex md:items-center md:justify-between md:p-6">
    <span className="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2024 <a href="https://github.com/Percival33/BHL2024"
                                                                                        className="hover:underline">Ale to ty dzwonisz!?™</a>
    </span>
      <ul className="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
        <li>
          <a href="https://github.com/Percival33/BHL2024" className="hover:underline">Source code</a>
        </li>
      </ul>
    </footer>
  )
}