import Cookies from "js-cookie";

const BASE_URL = "http://127.0.0.1:8000";
export const getAllMembers = async (params = {}, maxRetries = 3) => {
  const token = Cookies.get("sub");
  const { first_name, status, page = 1, per_page = 20 } = params;

  const queryParams = new URLSearchParams();
  if (first_name) queryParams.append("first_name", first_name);
  if (status) queryParams.append("status", status);
  queryParams.append("page", page);
  queryParams.append("per_page", per_page);

  const url = `${BASE_URL}/members/?${queryParams.toString()}`;
  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  };

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url, options);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.warn(`Attempt ${attempt}/${maxRetries} failed:`, error.message);

      if (attempt === maxRetries) {
        throw new Error(
          `Failed after ${maxRetries} attempts: ${error.message}`
        );
      }

      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }
};
