import '../styles/globals.css';

export const metadata = {
  title: 'Todo App',
  description: 'Simple task management application',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-50 min-h-screen">
        <div className="min-h-screen">
          {children}
        </div>
      </body>
    </html>
  );
}