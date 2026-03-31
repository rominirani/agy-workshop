import "./globals.css";

export const metadata = {
  title: "Modern Analytics",
  description: "Advanced Bug-Fixing Workshop",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
