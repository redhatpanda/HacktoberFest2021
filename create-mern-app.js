console.log("Loading...");
console.log("Setting up Backend, Please Wait :)");
const { exec } = require("child_process");
const { mkdirSync, writeFile, readFileSync } = require("fs");

const handleErr = (err) => {
   if (err) {
      console.error(err);
      return;
   }
};

const handleExec = (error, stdout, stderr) => {
   if (error) {
      console.log(`error: ${error.message}`);
      return;
   }
   if (stderr) {
      console.log(`stderr: ${stderr}`);
      return;
   }
   console.log(`stdout: ${stdout}`);
};

["Controllers", "Models", "Routers", "Middleware"].map((folder) => {
   mkdirSync("./Server/" + folder, { recursive: true });
});

const serverJS = `const express = require(\"express\");
const morgan = require(\"morgan\");
const mongoose = require(\"mongoose\");
const { json, urlencoded } = require(\"body-parser\");
const path = require(\"path\");
const cors = require(\"cors\");

const app = express();

app.use(morgan(\"dev\"));
app.use(cors());
app.use(json());
app.use(urlencoded({ extended: true }));

const port = 3000;

app.listen(port, () => console.log(\"http://localhost:\" + port));`;

writeFile("./Server/server.js", serverJS, handleErr);
writeFile("./Server/Middleware/auth.js", "//Your Auth Code", handleErr);

exec(
   "cd Server && npm init -y && npm install express mongoose body-parser cors && npm install -D morgan && echo Setting up Frontend, Please Wait :)",
   handleExec
);

[
   "Assets",
   "Assets/CSS",
   "src/Components",
   "src/Hooks",
   "src/Utilities",
   "src/Pages",
].map((folder) => {
   mkdirSync("./Client/" + folder, { recursive: true });
});

const AppJSX = `import React from \"react\";
import { render } from \"react-dom\";
import { BrowserRouter as Router, Route, Switch } from \"react-router-dom\";
import { ErrorBoundary } from \"react-error-boundary\";
import { ErrorFallback } from \"./index.js\";

// eslint-disable-next-line no-unused-vars
const HandleErrorFallback = ({ error }) => {
   return <ErrorFallback />;
};

const App = () => {
   return (
      <Router>
         <ErrorBoundary FallbackComponent={HandleErrorFallback}>
            <Switch>
               <Route path=\"/\">
                  <div>Hello World</div>
               </Route>
            </Switch>
         </ErrorBoundary>
      </Router>
   );
};

render(<App />, document.getElementById(\"root\"));
`;

const EFJSX = `import React from \"react\";

const ErrorFallback = () => {
   return <div>Oops, Something went Wrong 😕</div>;
};

export default ErrorFallback;
`;

const ESLint = `{
   \"env\": {
       \"browser\": true,
       \"es2021\": true
   },
   \"extends\": [
       \"eslint:recommended\",
       \"plugin:react/recommended\"
   ],
   \"parserOptions\": {
       \"ecmaFeatures\": {
           \"jsx\": true
       },
       \"ecmaVersion\": 12,
       \"sourceType\": \"module\"
   },
   \"plugins\": [
       \"react\"
   ],
   \"rules\": {
       \"react/prop-types\": 0,
       \"react/react-in-jsx-scope\": 0,
       \"no-unused-vars\" : 1,
       \"no-undef\" : 1,
       \"react/jsx-no-undef\": 1
   }
}`;
writeFile("./Client/src/App.jsx", AppJSX, handleErr);

writeFile("./Client/src/Pages/ErrorFallback.jsx", EFJSX, handleErr);

writeFile(
   "./Client/src/index.js",
   'export { default as ErrorFallback } from "./Pages/ErrorFallback.jsx"',
   handleErr
);

writeFile(
   "./Client/.babelrc",
   `{
   \"presets\": [
		\"@babel/preset-env\",
		\"@babel/preset-react\"
   ]
}`,
   handleErr
);

writeFile("./Client/.eslintrc.json", ESLint, handleErr);

const indexHTML = `<!DOCTYPE html>
<html lang=\"en\">
   <head>
      <meta charset=\"UTF-8\" />
      <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\" />
      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
      <title>your Project</title>
   </head>
   <body>
      <div id=\"root\" class=\"flex-center\"></div>
   </body>
</html>`;

writeFile("./Client/index.html", indexHTML, handleErr);

const webpackConfig = `const path = require(\"path\");
const HtmlWebpackPlugin = require(\"html-webpack-plugin\");

module.exports = (env) => {
   const isProduction = env === \"production\";
   return {
      entry: \"./src/App.jsx\",
      output: {
         path: path.resolve(__dirname, \"build\"),
         publicPath: \"/\",
         filename: \"bundle.js\",
      },
      resolve: {
         alias: {
            components: path.resolve(__dirname, \"src\"),
         },
         extensions: [\".js\", \".jsx\"],
      },
      devServer: {
         static: \"./build\",
         historyApiFallback: true,
         proxy: {
            \"/api": \"http://localhost:3000\",
         },
      },
      module: {
         rules: [
            {
               test: /\.(js|jsx)$/,
               exclude: /node_modules/,
               use: [\"babel-loader\", \"eslint-loader\"],
            },
            {
               test: /\.css$/,
               use: [\"style-loader\", \"css-loader\"],
            },
            {
               test: /\.(png|svg|jpg|jpeg|gif)$/i,
               type: \"asset/resource\",
            },
            {
               test: /\.(woff|woff2|eot|ttf|otf)$/i,
               type: \"asset/resource\",
            },
         ],
      },
      plugins: [
         new HtmlWebpackPlugin({
            template: path.resolve(\"./index.html\"),
         }),
      ],
      devtool: isProduction ? \"source-map\" : \"inline-source-map\",
   };
};`;

writeFile("./Client/webpack.config.js", webpackConfig, handleErr);

const addScript = () => {
   let data = readFileSync("./Client/package.json", {
      encoding: "utf8",
      flag: "r",
   });
   data = data.replace(
      `exit 1\"`,
      `exit 1\", \"start\": \"webpack serve  --mode development --env=development\"`
   );
   writeFile("./Client/package.json", data, handleErr);
};
exec(
   "cd Client && npm init -y && npm install react react-dom react-error-boundary react-router-dom && npm install -D @babel/eslint-parser babel-loader @babel/core @babel/preset-env @babel/preset-react css-loader eslint eslint-config-react eslint-loader eslint-plugin-react webpack webpack-cli webpack-dev-server html-loader html-webpack-plugin style-loader url-loader",
   function (error, stdout, stderr) {
      addScript();
      handleExec(error, stdout, stderr);
      console.log("Done, Go Ahead and Make something Awesome!");
   }
);
