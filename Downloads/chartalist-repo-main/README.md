# Chartalist

Chartalist is a web platform for exploring, analyzing, and visualizing blockchain graph datasets. It provides labeled datasets from major blockchain networks to accelerate research in blockchain analytics and machine learning.

## Features

- **Dataset Catalog**: Browse curated blockchain datasets across major chains
- **Advanced Search**: Full-text search with filters by chain, task, size, and instance count
- **Interactive Explorer**: Sortable tables with detailed statistics and download tracking
- **Rich Documentation**: Dataset descriptions with citations and related datasets
- **Dark Mode Support**: Persistent theme preferences with system detection
- **Mobile Responsive**: Optimized for all screen sizes
- **Professional Design**: Academic-focused UI with smooth animations

## Tech Stack

- React 18 + TypeScript + Vite
- Tailwind CSS + shadcn/ui components
- React Router v6
- Client-side search and filtering
- React Query for data fetching

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm

### Installation & Local Setup

```bash
# Clone the repository
git clone https://github.com/chartalist/chartalist.git
cd chartalist

# Install dependencies
npm install

# Start development server
npm run dev
```

## Project Structure

```
src/
├── api/           # API utilities
├── assets/        # Images and tables for charts
├── components/    # Reusable UI components
│   └── ui/        # shadcn/ui components
├── content/       # MDX documentation for datasets/tasks
│   ├── bitcoin/
│   └── ethereum/
├── data/          # Static dataset catalog (datasets.json)
├── hooks/         # Custom React hooks
├── lib/           # Utility functions
├── pages/         # Route components for each feature/page
├── App.tsx        # Main app component
├── main.tsx       # Entry point
└── index.css      # Global styles
public/
├── files/         # Example CSVs and data files
├── images/        # Dataset and chart images
├── PHPMailer/     # Email utility (for contact/support)
```

## Key Pages & Routes

- `/` — Homepage
- `/datasets` — Dataset explorer
- `/datasets/:id` — Dataset details
- `/address-exclusion` — Privacy tool

## Data

- Images for datasets/charts are in `public/images/` and `src/assets/images/`

## Build & Deploy to Production

To build and deploy the app for production:

```bash
# Build for production
npm run build

# Preview the production build locally
npm run preview
```

The production-ready files will be in the `dist/` folder.

No environment variables are required for basic functionality. The app runs entirely client-side with static JSON data.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit a Pull Request

## Support

- Email: support@chartalist.org

## Google reCAPTCHA Setup

The Address Exclusion form uses Google reCAPTCHA to prevent spam and abuse.

### How it works

- The frontend uses the `react-google-recaptcha` package and a site key in `/src/pages/AddressExclusion.tsx`.
- The backend verifies the reCAPTCHA token using the secret key in `/src/api/address-exclusion.ts`.

### Setup Instructions

1. Go to [Google reCAPTCHA Admin](https://www.google.com/recaptcha/admin) and register your site to get a **site key** and **secret key**.
2. In `/src/pages/AddressExclusion.tsx`, replace the value of `sitekey` in the `<ReCAPTCHA />` component with your own site key:
   ```tsx
   <ReCAPTCHA sitekey="YOUR_SITE_KEY" onChange={handleRecaptchaChange} />
   ```
3. In your backend environment, set the secret key as an environment variable:
   ```bash
   export RECAPTCHA_SECRET_KEY=your_secret_key
   ```
   Or add it to your `.env` file:
   ```env
   RECAPTCHA_SECRET_KEY=your_secret_key
   ```
4. The backend will automatically use this secret to verify reCAPTCHA responses.

## PHPMailer Setup (Address Exclusion Form)

The Address Exclusion form sends requests via email using PHPMailer.

### How it works

- When a user submits the Address Exclusion form, the backend sends an email to the configured recipient (e.g., support@chartalist.org) using PHPMailer.
- Email sending is handled in `/src/api/address-exclusion.ts`.

### Setup Instructions

1. Ensure you have valid SMTP credentials (e.g., Gmail, Outlook, or your own mail server).
2. Set the following environment variables in your backend environment or `.env` file:
   ```env
   EMAIL_USER=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   RECAPTCHA_SECRET_KEY=your_recaptcha_secret
   ```
3. The recipient address (e.g., support@chartalist.org) is set in the backend code or passed from the frontend. Update it as needed in `/src/api/address-exclusion.ts`.
4. Make sure the PHPMailer library is present in `public/PHPMailer/` if you use PHP for email handling, or use the Node.js `nodemailer` package as shown in the backend code.

### Notes

- Google reCAPTCHA: The frontend integration is present in `src/pages/AddressExclusion.tsx` using `react-google-recaptcha`, and the backend verification is handled in `src/api/address-exclusion.ts` using the secret key.
- Email sending: The backend uses Node.js `nodemailer` (not PHP's PHPMailer) in `src/api/address-exclusion.ts` to send emails to the configured recipient (e.g., `support@chartalist.org`). The `public/PHPMailer/` folder is present for legacy or alternative PHP email handling, but the main workflow uses `nodemailer`.
